class SentiJapAPI < Sinatra::Base
  post '/api/v1/sentence/?' do
    content_type 'application/json'
    new_data = JSON.parse(request.body.read)
    pScore, nScore, sentiment = SentimentAna.call(sentence: new_data['sentence'])
    if pScore
      {
        pScore: pScore,
        nScore: nScore,
        sentiment: sentiment
      }.to_json
    else
      halt 400, 'FAILED to analyze sentence'
    end
  end
end
