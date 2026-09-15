# 泛微OA 数据表: `info_reward`

- **所属模块**: `政务应用`
- **数据库表名**: `info_reward`
- **字段总数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `pathid` | 路径id | `integer` | - | 是 | - |
| 4 | `name` | 加分项名称 | `varchar2` | 256 | 是 | - |
| 5 | `isused` | 是否启用 | `integer` | - | 是 | - |
| 6 | `rewardtype` | 加分项类型 | `integer` | - | 是 | 0加分项  1加分项组 2子加分项 |
| 7 | `mainid` | 加分项组id | `integer` | - | 是 | - |
| 8 | `arithtype` | 子项计算关系 | `integer` | - | 是 | 0累加 1取最高 2取最低 |
| 9 | `score` | 得分 | `float` | - | 是 | - |
| 10 | `isquick` | 是否快捷加分 | `integer` | - | 是 | - |
| 11 | `showinview` | 是否快捷展示到卡片 | `integer` | - | 是 | - |
| 12 | `showinlist` | 是否快捷展示到列表 | `integer` | - | 是 | - |
| 13 | `showname` | 显示名称 | `varchar2` | 256 | 是 | - |
| 14 | `isedit` | 是否允许修改分值 | `integer` | - | 是 | - |
| 15 | `isrepeat` | 是否允许重复加分 | `integer` | - | 是 | - |
| 16 | `isgroup1` | 是否根据刊型单独计分 | `integer` | - | 是 | - |
| 17 | `showlist1` | 刊型是否显示到列表 | `integer` | - | 是 | - |
| 18 | `showname1` | 显示名称 | `varchar2` | 256 | 是 | - |
| 19 | `isgroup2` | 是否根据栏目单独计分 | `integer` | - | 是 | - |
| 20 | `showlist2` | 栏目是否显示到列表 | `integer` | - | 是 | - |
| 21 | `showname2` | 显示名称 | `varchar2` | 256 | 是 | - |
| 22 | `showorder` | 显示顺序 | `float` | - | 是 | - |
