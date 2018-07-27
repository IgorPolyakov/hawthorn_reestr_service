# frozen_string_literal: trueaction_mailer

class UserMailer < ApplicationMailer
  def welcome_email
    @user = params[:user]
    @url = 'http://46.17.43.85:9999/'
    mail(to: @user.email, subject: 'Welcome to Hawthorn Reestr Service!')
  end
end
