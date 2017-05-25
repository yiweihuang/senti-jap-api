class SentimentAna
  def self.call(sentence:)
    info = `python helpers/sentiment_analysis.py "#{sentence}"`
    if info
      [info.split("\n")[0].to_f, info.split("\n")[1].to_f, info.split("\n")[2]]
    else
      nil
    end
  end
end
