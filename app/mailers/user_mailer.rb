# frozen_string_literal: trueaction_mailer

class UserMailer < ApplicationMailer
  def welcome_email
    @user = params[:user]
    @url = 'http://46.17.43.85:9999/'
    mail(to: @user.email, subject: 'Welcome to Hawthorn Reestr Service!')
  end
  def rosreesrt_request_done
    @user = params[:user]
    @search_query = params[:search_query]
    email = 'igorpolyakov@protonmail.com' # @user.email
    mail(to: email, subject: 'SearchQuery is done')
  end
end
