# frozen_string_literal: true

class RegisterService
  include Sidekiq::Worker

  def perform(search_query_id)
    search_query = SearchQuery.find(search_query_id)
    Rails.logger.info { "Run RegisterService: python3 #{Rails.root.join('hwsdk', 'RegisterService.py')} -v -q '#{search_query.to_json}'" }
    `python3 #{Rails.root.join('hwsdk', 'RegisterService.py')} -v -q '#{search_query.to_json}'`
  rescue Mongoid::Errors::DocumentNotFound
    Rails.logger.info { "Someone remove SearchQuery - #{search_query_id}. #{self.class} caught #{e.inspect}" }
  end
end
