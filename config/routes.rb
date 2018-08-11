# frozen_string_literal: true

require 'sidekiq/web'
Rails.application.routes.draw do
  devise_for :users
  resources :archive_queries, only: %i[index show]
  resources :search_queries do
    resources :locations, only: %i[update show] do
      member do
        get :download
      end
    end
    member do
      get :log
    end
  end
  root 'search_queries#index'
  mount Sidekiq::Web => '/sidekiq'
end
