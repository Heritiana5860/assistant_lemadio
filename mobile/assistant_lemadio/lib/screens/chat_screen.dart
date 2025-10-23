import 'package:flutter/material.dart';
import '../config/constants.dart';
import '../models/message.dart';
import '../services/api_service.dart';
import '../widgets/message_bubble.dart';
import '../widgets/input_field.dart';
import '../widgets/typing_indicator.dart';

/// Écran principal de conversation avec le chatbot
class ChatScreen extends StatefulWidget {
  final String? initialMessage;

  const ChatScreen({Key? key, this.initialMessage}) : super(key: key);

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final List<Message> _messages = [];
  final ApiService _apiService = ApiService();
  final ScrollController _scrollController = ScrollController();

  bool _isLoading = false;
  String? _errorMessage;

  @override
  void initState() {
    super.initState();

    // Si un message initial est fourni, l'envoyer automatiquement
    if (widget.initialMessage != null) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        _sendMessage(widget.initialMessage!);
      });
    }
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  /// Envoie un message au chatbot
  Future<void> _sendMessage(String text) async {
    if (text.trim().isEmpty) return;

    // Ajouter le message utilisateur
    final userMessage = Message.user(text);
    setState(() {
      _messages.add(userMessage);
      _isLoading = true;
      _errorMessage = null;
    });

    // Scroller vers le bas
    _scrollToBottom();

    try {
      // Appeler l'API
      final botMessage = await _apiService.sendMessage(text);

      // Ajouter la réponse du bot
      setState(() {
        _messages.add(botMessage);
        _isLoading = false;
      });

      // Scroller vers le bas
      _scrollToBottom();
    } catch (e) {
      // Gérer l'erreur
      setState(() {
        _isLoading = false;
        _errorMessage = e.toString().replaceAll('Exception: ', '');
      });

      // Afficher un message d'erreur
      _showErrorSnackBar(_errorMessage!);
    }
  }

  /// Scroll automatique vers le bas
  void _scrollToBottom() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeOut,
        );
      }
    });
  }

  /// Affiche un message d'erreur
  void _showErrorSnackBar(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: AppColors.error,
        action: SnackBarAction(
          label: 'Réessayer',
          textColor: Colors.white,
          onPressed: () {
            if (_messages.isNotEmpty && _messages.last.isUser) {
              _sendMessage(_messages.last.text);
            }
          },
        ),
        duration: const Duration(seconds: 5),
      ),
    );
  }

  /// Efface la conversation
  void _clearConversation() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Effacer la conversation ?'),
        content: const Text(
          'Tous les messages seront supprimés. Cette action est irréversible.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Annuler'),
          ),
          TextButton(
            onPressed: () {
              setState(() {
                _messages.clear();
              });
              Navigator.pop(context);
            },
            style: TextButton.styleFrom(foregroundColor: AppColors.error),
            child: const Text('Effacer'),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        foregroundColor: Colors.white,
        elevation: 0,
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            Text(
              'Assistant ADES',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            Text(
              'Toujours prêt à aider',
              style: TextStyle(fontSize: 12, color: Colors.white70),
            ),
          ],
        ),
        actions: [
          if (_messages.isNotEmpty)
            IconButton(
              icon: const Icon(Icons.delete_outline),
              onPressed: _clearConversation,
              tooltip: 'Effacer la conversation',
            ),
        ],
      ),
      body: Column(
        children: [
          // Liste des messages
          Expanded(
            child: _messages.isEmpty
                ? _buildEmptyState()
                : ListView.builder(
                    controller: _scrollController,
                    padding: const EdgeInsets.symmetric(
                      vertical: AppSizes.paddingSmall,
                    ),
                    itemCount: _messages.length + (_isLoading ? 1 : 0),
                    itemBuilder: (context, index) {
                      if (index == _messages.length) {
                        return const TypingIndicator();
                      }
                      return MessageBubble(message: _messages[index]);
                    },
                  ),
          ),

          // Champ de saisie
          InputField(onSend: _sendMessage, isLoading: _isLoading),
        ],
      ),
    );
  }

  /// État vide (quand il n'y a pas de messages)
  Widget _buildEmptyState() {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(AppSizes.paddingLarge),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: const EdgeInsets.all(AppSizes.paddingLarge),
              decoration: BoxDecoration(
                color: AppColors.primary.withOpacity(0.1),
                shape: BoxShape.circle,
              ),
              child: const Icon(
                Icons.chat_bubble_outline,
                size: 64,
                color: AppColors.primary,
              ),
            ),

            const SizedBox(height: AppSizes.paddingLarge),

            const Text(
              AppStrings.emptyChat,
              style: AppTextStyles.heading2,
              textAlign: TextAlign.center,
            ),

            const SizedBox(height: AppSizes.paddingSmall),

            const Text(
              'Posez votre première question sur l\'application ADES',
              style: AppTextStyles.bodySmall,
              textAlign: TextAlign.center,
            ),

            const SizedBox(height: AppSizes.paddingLarge),

            // Suggestions rapides
            Wrap(
              alignment: WrapAlignment.center,
              spacing: 8,
              runSpacing: 8,
              children: [
                _buildQuickSuggestion('Comment créer une vente ?'),
                _buildQuickSuggestion('Types de réchauds'),
                _buildQuickSuggestion('Comment annuler ?'),
              ],
            ),
          ],
        ),
      ),
    );
  }

  /// Widget pour une suggestion rapide
  Widget _buildQuickSuggestion(String text) {
    return InkWell(
      onTap: () => _sendMessage(text),
      borderRadius: BorderRadius.circular(20),
      child: Container(
        padding: const EdgeInsets.symmetric(
          horizontal: AppSizes.paddingMedium,
          vertical: AppSizes.paddingSmall,
        ),
        decoration: BoxDecoration(
          color: AppColors.cardBackground,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: AppColors.primary.withOpacity(0.3)),
        ),
        child: Text(
          text,
          style: const TextStyle(fontSize: 14, color: AppColors.primary),
        ),
      ),
    );
  }
}
