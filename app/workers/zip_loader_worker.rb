# frozen_string_literal: true

class ZipLoaderWorker
  include Sidekiq::Worker

  def perform(search_query_id, location_id)
    search_query = SearchQuery.find(search_query_id)
    location = search_query.locations.find(location_id)
    data = {}

    data[:id] = search_query_id
    data[:location_id] = location_id
    data[:search_uid] = location.search_uid

    text = "python3 #{Rails.root.join('selenium_py', 'zip_loader.py')} -v -http -q '[#{data.to_json}]'"
    pp text
    system(text)
    status = SearchQuery.find(search_query_id).locations.find(location_id).status
    raise 'wait for zip archive' unless status == 'готово'
  end
end
