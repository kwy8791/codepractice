以下2つの[出典](https://uxmilk.jp/12947)

- コマンドライン引数の取り方
```
puts $0: #{$0}2
ARGV.each_with_index do |arg, i|
  puts "ARGV[#{i}]：#{arg}"
end
```

```
$ ruby sample.rb hoge piyo
$0：sample.rb
ARGV[0]：hoge
ARGV[1]：piyo
```

- コマンドライン引数のファイルを読み込む
```
f = open(ARGV[0])
while line = f.gets
  print line
end
f.close
```
```
$ ruby sample.rb sample.rb 
f = open(ARGV[0])
while line = f.gets
  print line
end
```

