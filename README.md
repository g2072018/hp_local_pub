# 関研究室のホームページ


## 開発情報
基本的にfeature/OO のブランチで編集を行いdevelopブランチに統合（マージ）する．  
developブランチで一度完成版ができたらmainに統合する．

## ブランチについて
- main  
　リリースした時点のソースコードを管理するブランチ

- develop (mainから派生)  
　開発作業の主軸となるブランチ

- feature (developから派生)  
　実装する機能毎のブランチ (feature/◯◯, feature/xxなど)

- release (developから派生)  
　developでの開発作業完了後、リリース時の微調整を行うブランチ
　(バージョン番号の変更などで使いました。)

- hotfix (masterから派生)  
　リリースされた製品に致命的なバグ(クラッシュなど)があった場合に緊急対応をするためのブランチ  

イメージ画像（画像でmasterの部分はmainとして考える）
![](https://i.imgur.com/P2edBSY.png)

参考：Gitのブランチモデルについて - Qiita，https://qiita.com/y-okudera/items/0b57830d2f56d1d51692
