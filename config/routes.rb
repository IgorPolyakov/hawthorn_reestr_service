# frozen_string_literal: true

require 'sidekiq/web'
Rails.application.routes.draw do
  resources :search_queries, except: :edit do
    resources :locations, only: %i[update show] do
      member do
        get :download
      end
    end
  end
  root 'search_queries#index'
  mount Sidekiq::Web => '/sidekiq'
end
