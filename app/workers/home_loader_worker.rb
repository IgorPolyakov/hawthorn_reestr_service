# frozen_string_literal: true

class HomeLoaderWorker
  include Sidekiq::Worker

  def perform(search_query_id, location_id)
    search_query = SearchQuery.find(search_query_id)
    location = search_query.locations.find(location_id)
    data = {}

    data[:id] = search_query_id
    data[:location_id] = location_id
    data[:kdastr_id] = location.kdastr_id == '' ? nil : location.kdastr_id # null
    data[:use_kdastr] = location.use_kdastr == '' ? nil : location.use_kdastr # false
    data[:region] = location.region == '' ? nil : location.region # "Томская область"
    data[:district] = location.district == '' ? nil : location.district # null
    data[:populated_area] = location.populated_area == '' ? nil : location.populated_area # null
    data[:street_type] = location.street_type == '' ? nil : location.street_type # "Улица"
    data[:street_name] = location.street_name == '' ? nil : location.street_name # "Красноармейская"
    data[:house_number] = location.house_number == '' ? nil : location.house_number # "148"
    data[:apartment] = location.apartment == '' ? nil : location.apartment # "26"

    text = "python3 #{Rails.root.join('selenium_py', 'home_loader.py')} -v -http -q '[#{data.to_json}]'"
    pp text
    system(text)

    status = SearchQuery.find(search_query_id).locations.find(location_id).status
    # unless (status == 'в обработке') || (status == 'готово')
    #   raise "try to get 'search_uid'"
    # end
  end
end
