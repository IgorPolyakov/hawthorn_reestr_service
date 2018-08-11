# frozen_string_literal: true

class SearchQuery
  include Mongoid::Document
  include Mongoid::Timestamps
  field :title, type: String
  field :status, type: String, default: 'process'
  field :archive, type: Boolean, default: false
  field :log_path, type: String, default: ''
  belongs_to :user
  embeds_many :locations
  accepts_nested_attributes_for :locations
  after_save :remove_finished
  scope :archive, -> { where(archive: true) }
  scope :active, -> { where(archive: false) }

  def log
    File.exist?(log_path) ? File.read(log_path) : 'Нет доступных журналов'
  end

  def counter
    wait_status = ['запуск', 'в обработке']
    done_status = %w[готово ошибка закончено]
    total = locations.inject(0) { |sum, loc| wait_status.any?(loc.status) ? sum : sum + 1 }
    "#{total}/#{locations.count}"
  end

  private

  def remove_finished
    locations.each do |location|
      location.delete if location.status == 'закончено'
    end
  end
end
