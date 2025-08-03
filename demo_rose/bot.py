import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
#                                              
# Đảm bảo bạn đã thêm MessageHandler vào đây
# Thay thế "YOUR_BOT_TOKEN_HERE" bằng token của bot bạn
BOT_TOKEN = "8257475534:AAH601BkqxL2fSI-ph8wSM1lG9JYiKEC_yQ"

# Cấu hình logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    
    
    if message.new_chat_members:
        # Bước 1: Xóa tin nhắn hệ thống "đã tham gia nhóm"
        try:
            await message.delete()
            logging.info("Deleted system message about new member.")
        except Exception as e:
            logging.error(f"Failed to delete message: {e}")
            
        # Bước 2: Gửi tin nhắn chào mừng tùy chỉnh
        for member in message.new_chat_members:
            user_name = member.first_name
            # Có thể thêm logic để cá nhân hóa tin nhắn chào mừng ở đây
            
            # Tin nhắn chào mừng giống trong hình ảnh bạn gửi
            welcome_message = (
                f"Chào mừng {user_name} đã đến với NHÓM KÈO của BLV BOSSHAI1985 \n"
                f"👉 ĐĂNG KÍ TÀI KHOẢN CLICK BÊN DƯỚI HOẶC VÀO LINK  https://8x6342.com/n👉 BẢO HIỂM VỐN 100% VÉ ĐẦU VÀ 50% NẠP ĐẦU NHẮN CHO CSKH https://t.me/foden1440\n"
                f"👉 VÀO NHÓM SOI KÈO BẤM THAM GIA ✅CLICK NGAY 👇👇👇👇"
            )



            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=welcome_message
            )
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:        
    # 1. Tạo các nút bấm
    # Mỗi nút là một đối tượng InlineKeyboardButton
    # Tham số 'text' là chữ hiển thị trên nút
    # Tham số 'url' là đường link sẽ được mở khi bấm nút
    keyboard = [
        [
            InlineKeyboardButton("Truy cập Website", url="https://8x6342.com"),
            InlineKeyboardButton("Kết nối Telegram", url="https://t.me/FODEN1440")
        ],
        [
            InlineKeyboardButton("NHẬN KHUYẾN MÃI", url="https://google.com")
        ]
    ]    
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Lắng nghe sự kiện thành viên mới vào
    new_member_handler = MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_new_member)
    application.add_handler(new_member_handler)

    application.run_polling()

if __name__ == '__main__':
    main()