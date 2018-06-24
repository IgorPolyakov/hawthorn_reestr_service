# frozen_string_literal: true

class SearchQuery
  include Mongoid::Document
  include Mongoid::Timestamps
  field :title, type: String
  belongs_to :user
  embeds_many :locations
  accepts_nested_attributes_for :locations
  after_save :run_workers

  def status
    total = locations.inject(0) { |sum, loc| loc.status == 'готово' ? sum + 1 : sum }
    "#{total}/#{locations.count}"
  end

  private

  def run_workers
    locations.each do |location|
      if location.status == 'закончено'
        logger.info "Location with id #{location.id.to_s)} will be remove, in search_query #{id.to_s}"
        location.delete
      end
    end

    locations.each do |location|
      if location.status == 'запуск' && location.apartment.try(:empty?)
        logger.info "Home Loader Worker - Search Query: #{id.to_s}, Location: #{location.id.to_s)}"
        HomeLoaderWorker.perform_async(id.to_s, location.id.to_s)
      else
        logger.info "Query Sender Worker - Search Query: #{id.to_s}, Location: #{location.id.to_s)}"
        QuerySenderWorker.perform_async(id.to_s, location.id.to_s)
      end
    end
  end
end
