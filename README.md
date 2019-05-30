# saveloadimg

批量导入/导出主机上的docker images

## 导出镜像(到目录 /tmp/saved-docker-images/）

```python
python dockersave.py
```

## 导入镜像

```
ls -F /tmp/saved-docker-images/*.tar | awk '{cmd="docker load -i "$1;print(cmd);system(cmd)}'
```
