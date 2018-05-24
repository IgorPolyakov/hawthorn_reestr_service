# frozen_string_literal: true

Rails.application.routes.draw do
  resources :search_queries, except: :edit do
    resources :locations
  end
  root 'search_queries#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
