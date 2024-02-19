# frozen_string_literal: true

# Notebook
class Notebook
  def initialize(save_file)
    @file  = save_file
    @notes = {}
    @tags  = {}
  end

  def find_tags(*tags)
    matches = []
    tags.each { |tag| matches << @tags[tag] }
  end
end
