#!/usr/bin/env ruby
# frozen_string_literal: true

require 'liquid'

path = ARGV[0] || File.expand_path('../snippets/cart-bundle-promo-config.liquid', __dir__)
src = File.read(path)
Liquid::Template.parse(src)
puts "liquid_parse_ok path=#{path} gem=liquid/#{Liquid::VERSION}"
