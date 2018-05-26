# frozen_string_literal: true

class HardWorker
  include Sidekiq::Worker

  def perform(search_query_id, location_id)
    text = "curl -v -H \"Accept: application/json\" -H \"Content-type: application/json\"  -X PATCH -d ' {\"location\":{\"status\": \"готово\"}}' http://127.0.0.1:9999/search_queries/#{search_query_id}/locations/#{location_id}"
    system(text)
    # search_query = SearchQuery.find(search_query_id)
    # location = search_query.locations.find(location_id)
    # location.status = 'готово'
    # location.save
  end
end
