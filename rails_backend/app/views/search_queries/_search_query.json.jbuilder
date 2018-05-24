# frozen_string_literal: true

json.extract! search_query, :id, :title, :create_relation
json.url search_query_url(search_query, format: :json)
