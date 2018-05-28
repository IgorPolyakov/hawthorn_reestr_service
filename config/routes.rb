# frozen_string_literal: true

require 'sidekiq/web'
Rails.application.routes.draw do
  resources :search_queries, except: :edit do
    resources :locations, only: %i[update show]
  end
  root 'search_queries#index'
  mount Sidekiq::Web => '/sidekiq'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end