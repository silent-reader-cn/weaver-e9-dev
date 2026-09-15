/**
 * 泛微 Ecology 9 流程表单与移动端表单代码块标准 JS 模板 (WfForm API)
 * 应用场景：
 * 泛微 OA 表单设计器 -> 插入代码块 -> JavaScript
 * 用于实现字段联动、主子表实时计算、提交前校验拦截、动态显隐与必填控制
 */

// 确保在 WfForm 加载完成后执行
jQuery(document).ready(function () {
  if (typeof WfForm === 'undefined') {
    return;
  }

  console.log('=== [泛微表单代码块] 初始化执行 ===');

  // 1. 字段标识常量定义 (根据表单实际字段ID替换)
  const FIELD_APPLY_USER = 'field1201'; // 申请人
  const FIELD_UNIT_PRICE = 'field1202'; // 单价 (主表)
  const FIELD_COUNT = 'field1203';      // 数量 (主表)
  const FIELD_TOTAL_AMOUNT = 'field1204';// 总金额 (主表)
  const FIELD_REMARK = 'field1205';     // 备注

  // 明细表1 字段
  const DTL1_PRICE = 'field1301';       // 明细单价
  const DTL1_NUM = 'field1302';         // 明细数量
  const DTL1_SUBTOTAL = 'field1303';    // 明细小计

  // 2. 字段值变更联动监听 (单价或数量变化时，自动计算总金额)
  WfForm.bindFieldChangeEvent(`${FIELD_UNIT_PRICE},${FIELD_COUNT}`, function (obj, id, value) {
    const price = parseFloat(WfForm.getFieldValue(FIELD_UNIT_PRICE)) || 0;
    const count = parseFloat(WfForm.getFieldValue(FIELD_COUNT)) || 0;
    const total = (price * count).toFixed(2);

    // 赋值给总金额字段 (第4个参数为是否触发后续变更联动)
    WfForm.changeFieldValue(FIELD_TOTAL_AMOUNT, { value: total });
    console.log(`[自动联动计算] 单价: ${price}, 数量: ${count}, 计算总额: ${total}`);
  });

  // 3. 监听明细表1行增加/删除事件与行内计算
  WfForm.bindDetailFieldChangeEvent(`${DTL1_PRICE},${DTL1_NUM}`, function (id, rowIndex, value) {
    const rowPrice = parseFloat(WfForm.getFieldValue(`${DTL1_PRICE}_${rowIndex}`)) || 0;
    const rowNum = parseFloat(WfForm.getFieldValue(`${DTL1_NUM}_${rowIndex}`)) || 0;
    const rowSubtotal = (rowPrice * rowNum).toFixed(2);

    WfForm.changeFieldValue(`${DTL1_SUBTOTAL}_${rowIndex}`, { value: rowSubtotal });
  });

  // 4. 表单提交前校验拦截 (注册提交校验钩子)
  WfForm.registerCheckEvent(WfForm.OPER_SUBMIT, function (callback) {
    const totalAmount = parseFloat(WfForm.getFieldValue(FIELD_TOTAL_AMOUNT)) || 0;
    const remark = WfForm.getFieldValue(FIELD_REMARK);

    // 校验规则：总金额大于 10,000 时，必须填写备注说明
    if (totalAmount > 10000 && (!remark || remark.trim() === '')) {
      // 弹出泛微标准气泡提示并阻断提交
      WfForm.showMessage('【提交拦截】申请总金额超过 10,000 元，必须在备注中详细说明用途！', 2, 5);
      return false; // 阻断提交
    }

    // 校验通过，放行提交
    callback();
  });

  // 5. 动态设置字段状态 (1:只读, 2:编辑, 3:必填)
  // 如果金额超过 5000，设置备注为必填
  WfForm.bindFieldChangeEvent(FIELD_TOTAL_AMOUNT, function (obj, id, value) {
    const amount = parseFloat(value) || 0;
    if (amount > 5000) {
      WfForm.changeFieldAttr(FIELD_REMARK, 3); // 必填
    } else {
      WfForm.changeFieldAttr(FIELD_REMARK, 2); // 普通编辑
    }
  });
});
