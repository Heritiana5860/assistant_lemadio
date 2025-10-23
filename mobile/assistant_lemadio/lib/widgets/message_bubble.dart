import 'package:flutter/material.dart';
import '../models/message.dart';
import '../config/constants.dart';

/// Widget pour afficher un message dans le chat
class MessageBubble extends StatelessWidget {
  final Message message;

  const MessageBubble({Key? key, required this.message}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        horizontal: AppSizes.paddingMedium,
        vertical: AppSizes.paddingSmall,
      ),
      child: Row(
        mainAxisAlignment: message.isUser
            ? MainAxisAlignment.end
            : MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Avatar pour le bot (à gauche)
          if (!message.isUser) _buildAvatar(),

          const SizedBox(width: AppSizes.paddingSmall),

          // Bulle de message
          Flexible(
            child: Column(
              crossAxisAlignment: message.isUser
                  ? CrossAxisAlignment.end
                  : CrossAxisAlignment.start,
              children: [
                // Conteneur du message
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: AppSizes.paddingMedium,
                    vertical: AppSizes.paddingSmall + 4,
                  ),
                  decoration: BoxDecoration(
                    color: message.isUser
                        ? AppColors.userMessage
                        : AppColors.botMessage,
                    borderRadius: BorderRadius.only(
                      topLeft: const Radius.circular(AppSizes.borderRadius),
                      topRight: const Radius.circular(AppSizes.borderRadius),
                      bottomLeft: Radius.circular(
                        message.isUser ? AppSizes.borderRadius : 4,
                      ),
                      bottomRight: Radius.circular(
                        message.isUser ? 4 : AppSizes.borderRadius,
                      ),
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.1),
                        blurRadius: 4,
                        offset: const Offset(0, 2),
                      ),
                    ],
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Texte du message
                      Text(
                        message.text,
                        style: message.isUser
                            ? AppTextStyles.messageUser
                            : AppTextStyles.messageBot,
                      ),

                      // Badge RAG (si applicable)
                      if (!message.isUser && message.ragUsed) ...[
                        const SizedBox(height: 4),
                        _buildRagBadge(),
                      ],
                    ],
                  ),
                ),

                // Heure du message
                const SizedBox(height: 4),
                Text(
                  _formatTime(message.timestamp),
                  style: AppTextStyles.caption,
                ),
              ],
            ),
          ),

          const SizedBox(width: AppSizes.paddingSmall),

          // Avatar pour l'utilisateur (à droite)
          if (message.isUser) _buildAvatar(),
        ],
      ),
    );
  }

  /// Construit l'avatar
  Widget _buildAvatar() {
    return Container(
      width: 32,
      height: 32,
      decoration: BoxDecoration(
        color: message.isUser ? AppColors.userMessage : AppColors.primary,
        shape: BoxShape.circle,
      ),
      child: Icon(
        message.isUser ? Icons.person : Icons.smart_toy,
        color: Colors.white,
        size: AppSizes.iconSizeSmall,
      ),
    );
  }

  /// Badge indiquant que la réponse utilise RAG
  Widget _buildRagBadge() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
      decoration: BoxDecoration(
        color: AppColors.success.withOpacity(0.2),
        borderRadius: BorderRadius.circular(4),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: const [
          Icon(Icons.verified, size: 12, color: AppColors.success),
          SizedBox(width: 4),
          Text(
            'Basé sur la doc',
            style: TextStyle(
              fontSize: 10,
              color: AppColors.success,
              fontWeight: FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }

  /// Formate l'heure du message
  String _formatTime(DateTime timestamp) {
    final now = DateTime.now();
    final difference = now.difference(timestamp);

    if (difference.inMinutes < 1) {
      return 'À l\'instant';
    } else if (difference.inHours < 1) {
      return '${difference.inMinutes}min';
    } else if (difference.inDays < 1) {
      return '${timestamp.hour}:${timestamp.minute.toString().padLeft(2, '0')}';
    } else {
      return '${timestamp.day}/${timestamp.month} ${timestamp.hour}:${timestamp.minute.toString().padLeft(2, '0')}';
    }
  }
}
