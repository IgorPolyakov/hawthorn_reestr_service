# frozen_string_literal: true

class LocationsController < ApplicationController
  before_action :set_location, only: %i[index show update download log]
  skip_before_action :verify_authenticity_token
  # GET /locations
  # GET /locations.json
  def index
    @locations = @search_query.locations
  end

  # GET /locations/1
  # GET /locations/1.json
  def show; end

  # PATCH/PUT /locations/1
  # PATCH/PUT /locations/1.json
  def update
    if @location.update(location_params)
      render :show, status: :ok, local: @location
    else
      render json: @location.errors, status: :unprocessable_entity
    end
  end

  def download
    zip_file = @location.root_path
    if File.exist? zip_file
      send_file zip_file, disposition: 'attachment'
    else
      flash[:alert] = 'File not found'
      redirect_to root_path
    end
  end

  def log
    render json: { log: @location.log }
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_location
    @search_query = SearchQuery.find(params[:search_query_id])
    @location = @search_query.locations.find(params[:id])
  end

  # Never trust parameters from the scary internet, only allow the white list through.
  def location_params
    params
      .require(:location)
      .permit(
        :status,
        :search_uid,
        :zip_url,
        :root_path
      )
  end
end
