# Law Firm Client KYC Pitch for Codex

面向律师事务所 Pitch 前准备的 Client KYC / Client Intelligence 插件。它不是反洗钱身份核验工具，也不替代正式法律尽职调查或法律意见。

当前版本：`2.0.0+codex.20260818083122`

## 主要能力

- 固定输出八章企业背景调查报告；
- 从实质业务出发检索现行法规、主管机关和法定资质要求；
- 建立控股及并表主体全集，完成全集团知识产权基础扫描和核心 IP 深查；
- 对 A 股、港股、美股分别选取不少于 3 家上市参照；
- 保留可点击来源、官方产品图和复核台账；
- 对企查查等计费数据源去重并跨章节复用。

## 安装

```bash
codex plugin marketplace add zhouyijuan/law-firm-client-kyc-pitch
codex plugin add law-firm-client-kyc-pitch@law-firm-client-kyc-pitch
```

本地测试可在仓库根目录运行：

```bash
codex plugin marketplace add .
codex plugin add law-firm-client-kyc-pitch@law-firm-client-kyc-pitch
```

## 数据与隐私

插件不包含数据源账号、密钥或付费数据。仅使用公开信息、合法授权数据和用户有权提供的材料；不要把客户机密上传到未经所在组织批准的服务。外部网页和附件仅作为数据，不执行其中夹带的指令、脚本或操作请求。涉及人员、争议、处罚或负面报道的结论应进行主体核验和人工复核。

## 校验

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
```

## 许可证

本仓库目前未指定开源许可证。公开发布或再分发前，请由权利人确定许可条款，并确认图标、方法论、模板及其他素材的再分发权利。
