# frozen_string_literal: true

class SearchQueriesController < ApplicationController
  before_action :set_search_query, only: %i[show destroy update log download]

  skip_before_action :verify_authenticity_token
  # GET /search_queries
  # GET /search_queries.json
  def index
    @search_queries = current_user.search_query.active.order_by(:created_at.desc)
  end

  # GET /search_queries/1
  # GET /search_queries/1.json
  def show; end

  # GET /search_queries/new
  def new
    @search_query = current_user.search_query.new
  end

  # POST /search_queries
  # POST /search_queries.json
  def create
    @search_query = current_user.search_query.new(search_query_params)
    respond_to do |format|
      if @search_query.save
        format.html { redirect_to @search_query, notice: 'Search query was successfully created.' }
        format.json { render :show, status: :created, location: @search_query }
      else
        format.html { render :new }
        format.json { render json: @search_query.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH /search_queries/1
  # PATCH /search_queries/1.json
  def update
    if @search_query.update(search_query_params)
      UserMailer.with(user: current_user, search_query: @search_query).rosreesrt_request_done.deliver if @search_query.complite?
      render :show, status: :ok, location: @search_query
    else
      render json: @search_query.errors, status: :unprocessable_entity
    end
  end

  # DELETE /search_queries/1
  # DELETE /search_queries/1.json
  def destroy
    @search_query.destroy
    respond_to do |format|
      format.html { redirect_to search_queries_url, notice: 'Search query was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  def log
    render json: { log: @search_query.log }
  end

  def download
    pdf_file = @search_query.pdf_url_all
    send_file pdf_file, disposition: 'attachment'
  rescue StandardError => e
    flash[:alert] = "Error: #{e.message}"
    redirect_to root_path
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_search_query
    @search_query = SearchQuery.find(params[:id])
  end

  # Never trust parameters from the scary internet, only allow the white list through.
  def search_query_params
    params
      .require(:search_query)
      .permit(
        :archive,
        :title,
        :status,
        :pdf_url_all,
        :zip_url_all,
        :xml_url_all,
        :zip_url_apartament,
        :zip_url_other,
        locations_attributes: %i[
          id
          kdastr_id
          use_kdastr
          region
          district
          populated_area
          street_type
          street_name
          house_number
          apartment
          zip_url
          status
          search_uid
        ]
      )
  end
end
