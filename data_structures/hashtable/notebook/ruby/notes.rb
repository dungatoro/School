# frozen_string_literal: true

# Notebook
class Notebook
  def initialize(save_file)
    @file  = save_file
    @notes = {}
    @tags  = {}
  end

  def find_tags(*tags)
    tags.map { |tag| @tags[tag] }.flatten.uniq
  end

  def [](title)
    @notes[title] || "No note call #{title}"
  end

  def insert(title, text, tags)
    @notes[title] = text
    tags.each { |t| @tags.key?(t) ? @tags[t] << title : @tags[t] = [title] }
  end
end

n = Notebook.new('')
n.insert 'dogs', 'some dogs stuff', %w[animals pets]
n.insert 'cats', 'some cats stuff', %w[animals pets devils]
n.insert 'emus', 'some emus stuff', %w[creepy fake]
puts n['dogs']
puts n.find_tags('devils', 'creepy')
