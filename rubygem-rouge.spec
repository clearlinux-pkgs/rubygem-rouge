#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rouge
Version  : 1.11.0
Release  : 9
URL      : https://rubygems.org/downloads/rouge-1.11.0.gem
Source0  : https://rubygems.org/downloads/rouge-1.11.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-rouge-bin
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
No detailed description available

%package bin
Summary: bin components for the rubygem-rouge package.
Group: Binaries

%description bin
bin components for the rubygem-rouge package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rouge-1.11.0
gem spec %{SOURCE0} -l --ruby > rubygem-rouge.gemspec

%build
gem build rubygem-rouge.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rouge-1.11.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rouge-1.11.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/bin/rougify
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/actionscript
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/apache
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/apiblueprint
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/applescript
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/biml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/c
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/ceylon
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/clojure
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/cmake
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/coffeescript
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/common_lisp
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/conf
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/coq
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/cpp
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/csharp
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/css
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/d
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/dart
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/diff
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/eiffel
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/elixir
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/erb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/erlang
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/factor
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/fortran
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/gherkin
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/glsl
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/go
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/gradle
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/groovy
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/haml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/handlebars
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/haskell
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/html
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/http
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/ini
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/io
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/java
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/javascript
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/jinja
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/json
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/json-doc
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/jsonnet
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/julia
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/liquid
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/literate_coffeescript
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/literate_haskell
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/llvm
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/lua
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/make
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/markdown
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/matlab
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/moonscript
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/nasm
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/nginx
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/nim
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/objective_c
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/ocaml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/perl
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/php
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/plaintext
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/powershell
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/praat
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/prolog
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/properties
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/protobuf
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/puppet
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/python
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/qml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/r
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/racket
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/ruby
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/rust
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/sass
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/scala
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/scheme
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/scss
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/sed
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/shell
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/shell_session
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/slim
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/smalltalk
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/smarty
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/sml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/sql
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/swift
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/tap
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/tcl
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/tex
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/toml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/tulip
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/twig
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/typescript
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/vb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/verilog
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/viml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/xml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/demos/yaml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/formatters/html.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/formatters/html_wrapper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/formatters/null.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/formatters/terminal256.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/actionscript.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/apache.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/apache/keywords.yml
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/apiblueprint.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/apple_script.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/biml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/c.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/ceylon.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/clojure.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/cmake.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/coffeescript.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/common_lisp.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/conf.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/coq.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/cpp.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/csharp.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/css.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/d.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/dart.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/diff.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/eiffel.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/elixir.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/erb.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/erlang.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/factor.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/fortran.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/gherkin.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/gherkin/keywords.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/glsl.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/go.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/gradle.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/groovy.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/haml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/handlebars.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/haskell.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/html.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/http.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/ini.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/io.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/java.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/javascript.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/jinja.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/jsonnet.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/julia.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/liquid.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/literate_coffeescript.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/literate_haskell.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/llvm.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/lua.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/lua/builtins.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/make.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/markdown.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/matlab.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/matlab/builtins.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/moonscript.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/nasm.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/nginx.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/nim.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/objective_c.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/ocaml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/perl.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/php.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/php/builtins.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/plain_text.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/powershell.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/praat.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/prolog.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/properties.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/protobuf.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/puppet.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/python.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/qml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/r.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/racket.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/ruby.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/rust.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/sass.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/sass/common.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/scala.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/scheme.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/scss.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/sed.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/shell.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/shell_session.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/slim.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/smalltalk.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/smarty.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/sml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/sql.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/swift.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/tap.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/tcl.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/tex.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/toml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/tulip.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/twig.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/typescript.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/vb.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/verilog.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/viml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/viml/keywords.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/xml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/lexers/yaml.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/plugins/redcarpet.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/regex_lexer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/template_lexer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/text_analyzer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/theme.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/themes/base16.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/themes/colorful.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/themes/github.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/themes/molokai.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/themes/monokai.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/themes/monokai_sublime.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/themes/thankful_eyes.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/token.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/util.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/lib/rouge/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/rouge-1.11.0/rouge.gemspec
/usr/lib64/ruby/gems/2.3.0/specifications/rouge-1.11.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/rougify
