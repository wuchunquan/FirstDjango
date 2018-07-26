python3+django2.0 实现用户注册登录sessio记录和注销
遇到的问题是：git时，这个新版本库有readme文件，提交失败。于是用pull命令合并readme时，本地工作区就只剩下readme了，不过幸好暂存区还存在着之前的文件，但提交到远程仓库时依然失败，还是同样的问题，然后使用git push -f强制提交了，问题应该是在合并时出现了错误。
其他问题就是使用cookie失败，许多办法都试了还是失败，但用session成功了，在获得session时直接session[''],用get会出问题
