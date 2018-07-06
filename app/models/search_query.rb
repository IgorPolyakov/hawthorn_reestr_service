# frozen_string_literal: true

class SearchQuery
  include Mongoid::Document
  include Mongoid::Timestamps
  field :title, type: String
  field :status, type: String, default: 'process'
  belongs_to :user
  embeds_many :locations
  accepts_nested_attributes_for :locations
  after_save :run_workers

  def counter
    wait_status = ['запуск', 'в обработке']
    done_status = %w[готово ошибка закончено]
    total = locations.inject(0) { |sum, loc| wait_status.any?(loc.status) ? sum : sum + 1 }
    "#{total}/#{locations.count}"
  end

  private

  def run_workers
    locations.each do |location|
      location.delete if location.status == 'закончено'
    end

    locations.each do |location|
      if location.status == 'запуск' && location.apartment.try(:empty?)
        HomeLoaderWorker.perform_async(id.to_s, location.id.to_s)
      else
        QuerySenderWorker.perform_async(id.to_s, location.id.to_s)
      end
    end
  end
end
