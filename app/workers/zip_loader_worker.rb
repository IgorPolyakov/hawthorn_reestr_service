# frozen_string_literal: true

class ZipLoaderWorker
  include Sidekiq::Worker
  class NotReady < StandardError
  end
  def perform(search_query_id, location_id)
    search_query = SearchQuery.find(search_query_id)
    location = search_query.locations.find(location_id)
    data = {}

    data[:id] = search_query_id
    data[:location_id] = location_id
    data[:search_uid] = location.search_uid

    Rails.logger.info { "Run Zip Loader: python3 #{Rails.root.join('selenium_py', 'zip_loader.py')} -v -http -q '[#{data.to_json}]'" }
    `python3 #{Rails.root.join('selenium_py', 'zip_loader.py')} -v -http -q '[#{data.to_json}]'`
    status = SearchQuery.find(search_query_id).locations.find(location_id).status
    raise ZipNotReady, 'wait for zip archive' unless status == 'готово'
  rescue ZipNotReady
    Rails.logger.info { "Zip archive not ready. #{self.class} caught #{e.inspect}" }
    ZipLoaderWorker.perform_in(5.minutes, search_query_id, location_id)
  rescue Mongoid::Errors::DocumentNotFound
    Rails.logger.info { "Someone remove SearchQuery - #{search_query_id}. Location - #{location_id}. #{self.class} caught #{e.inspect}" }
  end
end
