require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  HTMLProofer.check_directory("./_site", {
    :url_ignore => [/nemonein.egloos.com/], [/www.etnews.com/],
  }).run
end
