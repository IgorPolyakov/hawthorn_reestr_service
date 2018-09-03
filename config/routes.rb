# frozen_string_literal: true

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
end
