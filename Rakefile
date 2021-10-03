require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
end

task :build do
  system "env LANG=\"en_US.UTF-8\" bundle exec jekyll serve -l -o --drafts"
end
