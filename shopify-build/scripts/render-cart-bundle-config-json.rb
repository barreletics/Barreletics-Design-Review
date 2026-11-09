#!/usr/bin/env ruby
# frozen_string_literal: true

# Theme-style Liquid render smoke test: JS placeholders must survive in output.
require 'liquid'

path = ARGV[0] || File.expand_path('../snippets/cart-bundle-promo-config.liquid', __dir__)
src = File.read(path)
tpl = Liquid::Template.parse(src)
html = tpl.render(
  { 'settings' => {}, 'all_products' => {}, 'images' => {} },
  strict_variables: false,
  strict_filters: false
)

checks = [
  ['visualSavingsNudgeTemplate', '{{percent}}', 'Add one more pair to save {{percent}}%.', 'Add one more pair to save %.'],
  ['visualSavingsAppliedTemplate', '{{amount}}', "{{amount}}", "You're saving ."],
  ['visualSavingsPreviewTemplate', '{{amount}}', 'Your potential savings: {{amount}}', 'Your potential savings: ']
]

checks.each do |key, placeholder, must_include, stripped_mark|
  section = html
  abort "missing_key #{key}" unless section.include?(key)
  abort "stripped_#{key}" if section.include?(stripped_mark) && !section.include?(must_include)
  abort "no_placeholder_#{key}" unless section.include?(placeholder)
end

puts "rendered_config_ok path=#{path}"
