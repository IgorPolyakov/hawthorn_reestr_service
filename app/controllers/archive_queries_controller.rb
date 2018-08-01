# frozen_string_literal: true

class ArchiveQueriesController < ApplicationController
  before_action :set_search_query, only: %i[show destroy]

  skip_before_action :verify_authenticity_token
  # GET /search_queries
  # GET /search_queries.json
  def index
    @search_queries = current_user.search_query.archive.order_by(:created_at.desc)
  end

  # GET /search_queries/1
  # GET /search_queries/1.json
  def show; end

  # DELETE /search_queries/1
  # DELETE /search_queries/1.json
  def destroy
    @search_query.destroy
    respond_to do |format|
      format.html { redirect_to search_queries_url, notice: 'Search query was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_search_query
    @search_query = SearchQuery.find(params[:id])
  end
end
