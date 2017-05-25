require 'sinatra'

# Configuration Sharing Web Service
class SentiJapAPI < Sinatra::Base
  enable :logging

  get '/?' do
    'SentiJap web service is up and running at /api/v1'
  end
end
