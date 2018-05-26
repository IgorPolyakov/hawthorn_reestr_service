# frozen_string_literal: true

class HardWorker
  include Sidekiq::Worker

  def perform(search_query_id, location_id)
    search_query = SearchQuery.find(search_query_id)
    location = search_query.locations.find(location_id)
    location.status = 'готово'
    location.save
  end
end
