# frozen_string_literal: true

json.array! @search_queries, partial: 'search_queries/search_query', as: :search_query
