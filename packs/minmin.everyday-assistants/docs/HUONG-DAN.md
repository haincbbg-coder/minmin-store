# Gói `minmin.everyday-assistants`

3 trợ lý đứng riêng. Không cần workflow, gọi thẳng từ trang Trợ lý hoặc từ chat.

## Trợ lý và skill đã gắn

| Slug | Tên | Skill |
|---|---|---|
| `tl-thu-ky` | Thư ký | `email-inbox-triage` (cần `minmin.hermes-inbox-web`), `weekly-review-planning` (cần `minmin.hermes-productivity`), `query-wiki` (hệ thống), `notes` (hệ thống) |
| `tl-tom-tat` | Người tóm tắt | `document-to-action-items` (cần `minmin.hermes-office`), `meeting-action-items` (cần `minmin.hermes-office`), `notes` (hệ thống) |
| `tl-phan-bien` | Người phản biện | `grounded-citations` (cần `minmin.hermes-research`), `verification-before-completion` (cần `minmin.superpowers`), `query-wiki` (hệ thống) |

Skill ghi **(hệ thống)** có sẵn trong mọi brain, không phải cài gì thêm.

Skill còn lại đến từ: `minmin.hermes-inbox-web`, `minmin.hermes-office`, `minmin.hermes-productivity`, `minmin.hermes-research`, `minmin.superpowers`. MinMin không có cơ chế khai phụ thuộc giữa các gói, nên chưa cài chúng thì trợ lý vẫn chạy: mỗi trợ lý được dạy là gọi skill không có thì đi tiếp bằng năng lực sẵn có rồi báo lại một dòng cho bạn biết thiếu gì.

## Chỗ bạn nên chỉnh sau khi cài

Mọi trợ lý để `model: ""`, tức chạy theo mặc định của engine bạn đang dùng. Ghim model cụ thể chỉ khi bạn chắc máy mình có model đó.

Trợ lý được ghi vào **brain đang mở lúc bấm Cài**, không phải mọi brain. MinMin không ghi đè trợ lý bạn tự tạo trùng tên, và gỡ gói chỉ xoá thứ bạn chưa sửa.
