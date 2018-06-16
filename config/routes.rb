# frozen_string_literal: true

require 'sidekiq/web'
Rails.application.routes.draw do
  devise_for :users
  resources :search_queries do
    resources :locations, only: %i[update show] do
      member do
        get :download
        get :log
      end
    end
  end
  root 'search_queries#index'
  mount Sidekiq::Web => '/sidekiq'
end
