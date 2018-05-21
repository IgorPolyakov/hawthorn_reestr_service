# frozen_string_literal: true

json.extract! search_query, :id, :search_uid, :created_at, :updated_at
json.url search_query_url(search_query, format: :json)
