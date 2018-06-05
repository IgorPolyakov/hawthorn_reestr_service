# frozen_string_literal: true

class SearchQuery
  include Mongoid::Document
  include Mongoid::Timestamps
  field :title, type: String
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
      if location.status == 'запуск' && location.apartment.try(:empty?)
        HomeLoaderWorker.perform_async(id.to_s, location.id.to_s)
      else
        QuerySenderWorker.perform_async(id.to_s, location.id.to_s)
      end
    end
  end
end
