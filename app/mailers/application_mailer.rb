# frozen_string_literal: true

class ApplicationMailer < ActionMailer::Base
  default from: 'fox_741@mail.ru'
  layout 'mailer'
end
