# 泛微OA 数据表: `social_pc_urlicons`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_pc_urlicons`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `labelindexid` | 多语言标签id | `integer` | - | 是 | 对应htmllabelinfo表 |
| 3 | `labeltemp` | 设置页面输入的按钮名称 | `varchar2` | 800 | 是 | 备用的中文标签名称 |
| 4 | `icouri` | 按钮图标地址 | `varchar2` | 800 | 是 | 按钮图标地址 |
| 5 | `hoticouri` | 高亮图标地址 | `varchar2` | 800 | 是 | 高亮图标地址 |
| 6 | `ifshowon` | 是否展示 | `char` | 1 | 是 | 是否展示，0不展示，1展示 |
| 7 | `showindex` | 展示顺序 | `integer` | - | 是 | 展示顺序 |
| 8 | `uritype` | 链接类型 | `integer` | - | 是 | 链接类型 |
| 9 | `linkuri` | 点击时打开的链接地址 | `varchar2` | 1000 | 是 | 点击时打开的链接地址 |
| 10 | `numberuri` | 角标数字获取地址 | `varchar2` | 1000 | 是 | 角标数字获取地址 |
| 11 | `icotype` | 应用类型 | `char` | 1 | 是 | 1代表底部应用，0代表顶部应用 |
| 12 | `ifsysico` | 是否是系统应用 | `char` | 1 | 是 | 1代表系统应用，0代表外部应用 |
