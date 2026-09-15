# 前端 JS API 总索引

> 共 **138** 个前端接口方法，覆盖流程表单 `WfForm` 与表单建模 `ModeForm`。

> 索引由 `scripts/build_index.py` 自动生成，请勿手工编辑。
> 检索请用统一检索脚本：
> ```bash
> python scripts/search.py convertFieldNameToId --scope js
> python scripts/search.py 明细表 --scope js
> ```

## 泛微OA (E-Cology 9) 表单建模前端 ModeForm API 开发全指南

> 文件：[`modeform.md`](./modeform.md)　共 `57` 个方法。

| 序号 | 方法说明 | 接口名 | 文件 |
| :---: | :--- | :--- | :--- |
| 1 | 2.1 将字段名称转换成字段id | `convertFieldNameToId` | [modeform.md](./modeform.md) |
| 2 | 2.2 获取单子字段值 | `getFieldValue` | [modeform.md](./modeform.md) |
| 3 | 2.3 修改单个字段值 | `changeFieldValue` | [modeform.md](./modeform.md) |
| 4 | 2.4 改变单个字段显示属性(只读/必填等) | `changeFieldAttr` | [modeform.md](./modeform.md) |
| 5 | 2.5 同时修改字段的值及显示属性 | `changeSingleField` | [modeform.md](./modeform.md) |
| 6 | 2.6 批量修改字段值或显示属性 | `changeMoreField` | [modeform.md](./modeform.md) |
| 7 | 3.1 添加明细及设置初始值 | `addDetailRow` | [modeform.md](./modeform.md) |
| 8 | 3.2 删除明细表指定行/全部行 | `delDetailRow` | [modeform.md](./modeform.md) |
| 9 | 3.3  选中明细指定行/全部行 | `checkDetailRow` | [modeform.md](./modeform.md) |
| 10 | 3.4  获取明细行所有行标示 | - | [modeform.md](./modeform.md) |
| 11 | 3.5 获取明细已有行的数据库主键 | `getDetailRowKey` | [modeform.md](./modeform.md) |
| 12 | 3.6  添加明细时默认复制最后一行记录 | `setDetailAddUseCopy` | [modeform.md](./modeform.md) |
| 13 | 3.7 根据明细行标识获取序号(第几行) | `getDetailRowSerailNum` | [modeform.md](./modeform.md) |
| 14 | 3.8 获取明细总行数 | - | [modeform.md](./modeform.md) |
| 15 | 3.9 控制明细数据行的显示及隐藏 | `controlDetailRowDisplay` | [modeform.md](./modeform.md) |
| 16 | 3.10 控制明细行check框是否禁用勾选 | `controlDetailRowDisableCheck` | [modeform.md](./modeform.md) |
| 17 | 3.11 获取明细选中行主键ID | - | [modeform.md](./modeform.md) |
| 18 | 3.12 获取明细选中行下标 | `appendBrowserDataUrlParam` | [modeform.md](./modeform.md) |
| 19 | 5.1  移除选择框字段选项 | `removeSelectOption` | [modeform.md](./modeform.md) |
| 20 | 5.2   控制选择框字段选项 | `controlSelectOption` | [modeform.md](./modeform.md) |
| 21 | 5.3 获取选择框字段的显示值 | `getSelectShowName` | [modeform.md](./modeform.md) |
| 22 | 6.1  表单顶部按钮、右键菜单置灰 | `controlBtnDisabled` | [modeform.md](./modeform.md) |
| 23 | 6.2  根据字段ID获取字段信息 | `getFieldInfo` | [modeform.md](./modeform.md) |
| 24 | 6.3  获取字段当前的只读/必填属性 | `getFieldCurViewAttr` | [modeform.md](./modeform.md) |
| 25 | 6.4  获取卡片的url参数 | `getCardUrlInfo` | [modeform.md](./modeform.md) |
| 26 | 6.5 刷新卡片当前页面 | `reloadCard` | [modeform.md](./modeform.md) |
| 27 | 6.6 外部调用卡片保存方法 | `doCardSubmit` | [modeform.md](./modeform.md) |
| 28 | 6.7 可控制显示时间的message信息 | `showMessage` | [modeform.md](./modeform.md) |
| 29 | 6.8 系统样式的Confirm确认框 | `showConfirm` | [modeform.md](./modeform.md) |
| 30 | 6.9 系统样式的Modal弹出框 | `showModalMsg` | [modeform.md](./modeform.md) |
| 31 | 6.10 调用右键按钮事件 | `doRightBtnEvent` | [modeform.md](./modeform.md) |
| 32 | 6.11、侧滑打开页面 | `slideOpenModal` | [modeform.md](./modeform.md) |
| 33 | 6.12、扩展提交操作发送给服务端的参数 | `appendSubmitParam` | [modeform.md](./modeform.md) |
| 34 | 7.1 提交事件执行自定义函数 | - | [modeform.md](./modeform.md) |
| 35 | 7.2 字段值变化触发事件bindPropertyChange | - | [modeform.md](./modeform.md) |
| 36 | 7.3 明细新增行渲染后触发事件 | - | [modeform.md](./modeform.md) |
| 37 | 7.4 明细删除行渲染后触发事件 | - | [modeform.md](./modeform.md) |
| 38 | 7.5 jQuery操作 | - | [modeform.md](./modeform.md) |
| 39 | 7.6  JS原生操作 | - | [modeform.md](./modeform.md) |
| 40 | 8.1  字段值变化触发事件 | `bindFieldChangeEvent` | [modeform.md](./modeform.md) |
| 41 | 8.2  明细字段值变化触发事件 | `bindDetailFieldChangeEvent` | [modeform.md](./modeform.md) |
| 42 | 9.1 窗口打开的两种方式 | - | [modeform.md](./modeform.md) |
| 43 | 10.1 获取当前用户信息 | `getCurrentUserInfo` | [modeform.md](./modeform.md) |
| 44 | 10.2  文本字段可编辑状态，当值为空显示默认灰色提示信息，鼠标点击输入时 提示消失 | `setTextFieldEmptyShowContent` | [modeform.md](./modeform.md) |
| 45 | 10.3  控制Radio框字段打印是否仅显示选中项文字 | `controlRadioPrintText` | [modeform.md](./modeform.md) |
| 46 | 10.4 获取保存按钮的页面扩展id | `getCardSubmitExpendId` | [modeform.md](./modeform.md) |
| 47 | 11.1 注册拦截事件，指定动作执行前触发，并可阻断/放行后续操作 | `registerCheckEvent` | [modeform.md](./modeform.md) |
| 48 | 11.2 注册钩子事件，指定动作完成后触发 | `registerAction` | [modeform.md](./modeform.md) |
| 49 | 12.1 字段区域绑定动作事件 | - | [modeform.md](./modeform.md) |
| 50 | 12.2  控制日期浏览按钮的可选日期范围 | `controlDateRange` | [modeform.md](./modeform.md) |
| 51 | 12.3  复写浏览按钮组件的props | `overrideBrowserProp` | [modeform.md](./modeform.md) |
| 52 | 12.4 自定义代理渲染单行文本框字段 | `proxyFieldComp` | [modeform.md](./modeform.md) |
| 53 | 12.5 自定义追加渲染表单字段 | `afterFieldComp` | [modeform.md](./modeform.md) |
| 54 | 12.6 函数式自定义渲染表单字段 | `proxyFieldContentComp` | [modeform.md](./modeform.md) |
| 55 | 12.7 根据字段标识获取字段组件 | `generateFieldContentComp` | [modeform.md](./modeform.md) |
| 56 | 13.1 页面loading | - | [modeform.md](./modeform.md) |
| 57 | 13.2 e9公共异步请求方法 | `clearChecked` | [modeform.md](./modeform.md) |

## 泛微OA (E-Cology 9) 流程表单前端 WfForm API 开发全指南

> 文件：[`wfform.md`](./wfform.md)　共 `81` 个方法。

| 序号 | 方法说明 | 接口名 | 文件 |
| :---: | :--- | :--- | :--- |
| 1 | 1.1 简介 | - | [wfform.md](./wfform.md) |
| 2 | 1.2 移动端兼容 | - | [wfform.md](./wfform.md) |
| 3 | 1.3 前端代码开发方式 | - | [wfform.md](./wfform.md) |
| 4 | 1.4 PC端打开表单的方式 | - | [wfform.md](./wfform.md) |
| 5 | 1.5 移动端打开表单的方式 | - | [wfform.md](./wfform.md) |
| 6 | 2.1 注册拦截事件，指定动作执行前触发，并可阻断/放行后续操作 | `registerCheckEvent` | [wfform.md](./wfform.md) |
| 7 | 2.2 注册钩子事件，指定动作完成后触发 | `registerAction` | [wfform.md](./wfform.md) |
| 8 | 3.1 将字段名称转换成字段id | `convertFieldNameToId` | [wfform.md](./wfform.md) |
| 9 | 3.2 获取单个字段值 | `getFieldValue` | [wfform.md](./wfform.md) |
| 10 | 3.3 修改单个字段值（不支持附件类型） | `changeFieldValue` | [wfform.md](./wfform.md) |
| 11 | 3.4 改变单个字段显示属性(只读/必填等) | `changeFieldAttr` | [wfform.md](./wfform.md) |
| 12 | 3.5 同时修改字段的值及显示属性 | `changeSingleField` | [wfform.md](./wfform.md) |
| 13 | 3.6 批量修改字段值或显示属性 | `changeMoreField` | [wfform.md](./wfform.md) |
| 14 | 3.7 触发指定字段涉及的所有联动（归档调用无效） | `triggerFieldAllLinkage` | [wfform.md](./wfform.md) |
| 15 | 3.8 根据字段ID获取字段信息 | `getFieldInfo` | [wfform.md](./wfform.md) |
| 16 | 3.9 获取字段当前的只读/必填属性 | `getFieldCurViewAttr` | [wfform.md](./wfform.md) |
| 17 | 4.1  表单字段值变化触发事件 | `bindFieldChangeEvent` | [wfform.md](./wfform.md) |
| 18 | 4.2  明细字段值变化触发事件 | `bindDetailFieldChangeEvent` | [wfform.md](./wfform.md) |
| 19 | 4.3 字段区域绑定动作事件 | `bindFieldAction` | [wfform.md](./wfform.md) |
| 20 | 4.4 自定义代理渲染单行文本框字段 | `proxyFieldComp` | [wfform.md](./wfform.md) |
| 21 | 4.5 自定义追加渲染表单字段 | `afterFieldComp` | [wfform.md](./wfform.md) |
| 22 | 4.6 函数式自定义渲染表单字段 | `proxyFieldContentComp` | [wfform.md](./wfform.md) |
| 23 | 4.7 根据字段标识获取字段组件 | `generateFieldContentComp` | [wfform.md](./wfform.md) |
| 24 | 5.1 添加明细行并设置初始值 | `addDetailRow` | [wfform.md](./wfform.md) |
| 25 | 5.2 删除明细表指定行/全部行 | `delDetailRow` | [wfform.md](./wfform.md) |
| 26 | 5.3 选中明细指定行/全部行 | `checkDetailRow` | [wfform.md](./wfform.md) |
| 27 | 5.4 获取明细行所有行标示 | - | [wfform.md](./wfform.md) |
| 28 | 5.5 获取明细选中行下标 | - | [wfform.md](./wfform.md) |
| 29 | 5.6 控制明细行check框是否禁用勾选 | `controlDetailRowDisableCheck` | [wfform.md](./wfform.md) |
| 30 | 5.7 控制明细数据行的显示及隐藏 | `controlDetailRowDisplay` | [wfform.md](./wfform.md) |
| 31 | 5.8 获取明细已有行的数据库主键 | `getDetailRowKey` | [wfform.md](./wfform.md) |
| 32 | 5.9 获取明细总行数 | - | [wfform.md](./wfform.md) |
| 33 | 5.10 添加行、删除行前执行逻辑或阻断事件 | - | [wfform.md](./wfform.md) |
| 34 | 5.11 添加行、删除行后触发事件 | - | [wfform.md](./wfform.md) |
| 35 | 5.12 移动端跳转至明细编辑行页面执行事件 | - | [wfform.md](./wfform.md) |
| 36 | 5.13  添加明细时默认复制最后一行记录 | `setDetailAddUseCopy` | [wfform.md](./wfform.md) |
| 37 | 5.14 根据明细行标识获取序号(第几行) | `getDetailRowSerailNum` | [wfform.md](./wfform.md) |
| 38 | 6.1 获取当前打开请求的基础信息 | `getBaseInfo` | [wfform.md](./wfform.md) |
| 39 | 6.2 可控制显示时间的message信息 | `showMessage` | [wfform.md](./wfform.md) |
| 40 | 6.3 系统样式的Confirm确认框 | `showConfirm` | [wfform.md](./wfform.md) |
| 41 | 6.4 表单顶部按钮、右键菜单置灰 | `controlBtnDisabled` | [wfform.md](./wfform.md) |
| 42 | 6.5 调用右键按钮事件 | `doRightBtnEvent` | [wfform.md](./wfform.md) |
| 43 | 6.6 刷新表单页面 | `reloadPage` | [wfform.md](./wfform.md) |
| 44 | 6.7 移动端打开链接方式 | - | [wfform.md](./wfform.md) |
| 45 | 6.8 扩展提交操作发送给服务端的参数 | `appendSubmitParam` | [wfform.md](./wfform.md) |
| 46 | 6.9 获取校验必填逻辑第一个未必填的字段 | `getFirstRequiredEmptyField` | [wfform.md](./wfform.md) |
| 47 | 6.10 触发一次必填验证 | `verifyFormRequired` | [wfform.md](./wfform.md) |
| 48 | 7.1 扩展浏览按钮取数接口参数值 | `appendBrowserDataUrlParam` | [wfform.md](./wfform.md) |
| 49 | 7.2 获取浏览按钮的显示值 | `getBrowserShowName` | [wfform.md](./wfform.md) |
| 50 | 7.3 移除选择框字段选项 | `removeSelectOption` | [wfform.md](./wfform.md) |
| 51 | 7.4 控制选择框字段选项 | `controlSelectOption` | [wfform.md](./wfform.md) |
| 52 | 7.5 获取选择框字段的显示值 | `getSelectShowName` | [wfform.md](./wfform.md) |
| 53 | 7.6 文本字段可编辑状态，当值为空显示默认灰色提示信息，鼠标点击输入时提示消失 | `setTextFieldEmptyShowContent` | [wfform.md](./wfform.md) |
| 54 | 7.7 复写浏览按钮组件的props | `overrideBrowserProp` | [wfform.md](./wfform.md) |
| 55 | 7.8 控制日期浏览按钮的可选日期范围 | `controlDateRange` | [wfform.md](./wfform.md) |
| 56 | 7.9 控制Radio框字段打印是否仅显示选中项文字 | `controlRadioPrintText` | [wfform.md](./wfform.md) |
| 57 | 8.1 获取签字意见内容 | `getSignRemark` | [wfform.md](./wfform.md) |
| 58 | 8.2 设置签字意见内容 | `setSignRemark` | [wfform.md](./wfform.md) |
| 59 | 8.3 扩展签字意见输入框底部按钮 | `appendSignEditorBottomBar` | [wfform.md](./wfform.md) |
| 60 | 9.1 提交事件执行自定义函数 | - | [wfform.md](./wfform.md) |
| 61 | 9.2 字段值变化触发事件bindPropertyChange | - | [wfform.md](./wfform.md) |
| 62 | 9.3 明细新增行渲染后触发事件 | - | [wfform.md](./wfform.md) |
| 63 | 9.4 明细删除行渲染后触发事件 | - | [wfform.md](./wfform.md) |
| 64 | 9.5 修改浏览按钮字段值window._writeBackData | - | [wfform.md](./wfform.md) |
| 65 | 9.6 少用jQuery操作 | - | [wfform.md](./wfform.md) |
| 66 | 9.7 禁止JS原生操作 | - | [wfform.md](./wfform.md) |
| 67 | 10.1 修改意见默认字体 | - | [wfform.md](./wfform.md) |
| 68 | 10.2 修改意见默认字体大小 | - | [wfform.md](./wfform.md) |
| 69 | 10.3 流程自定义浏览框缓存功能开关 | - | [wfform.md](./wfform.md) |
| 70 | 10.4 非多行文本html字段类型支持html格式 | - | [wfform.md](./wfform.md) |
| 71 | 10.5 PC端-流程表单显示底部耗时信息开个(调试分析用) | - | [wfform.md](./wfform.md) |
| 72 | 10.6 明细开启横向滚动条情况下，首行(按钮所在行)固定不跟随滚动条滚动 | - | [wfform.md](./wfform.md) |
| 73 | 10.7 明细字段合计给主字段，当明细未添加行，赋零值或空值 | - | [wfform.md](./wfform.md) |
| 74 | 10.8 pc端-手写签批按钮开关 | - | [wfform.md](./wfform.md) |
| 75 | 10.9 移动端-选择框单选框类型显示成radio效果开关 | - | [wfform.md](./wfform.md) |
| 76 | 10.10 移动端-表单正文、附件签批功能开关 | - | [wfform.md](./wfform.md) |
| 77 | 11.1 实现明细添加删除按钮靠左显示 | - | [wfform.md](./wfform.md) |
| 78 | 11.2 实现单元格图片居中、自适应缩放 | - | [wfform.md](./wfform.md) |
| 79 | 11.3 控制浏览按钮链接颜色 | - | [wfform.md](./wfform.md) |
| 80 | 11.4 控制主表选择框字段最小宽度 | - | [wfform.md](./wfform.md) |
| 81 | 12.1 移动端异构系统提交表单后，如何刷新流程列表 | - | [wfform.md](./wfform.md) |
