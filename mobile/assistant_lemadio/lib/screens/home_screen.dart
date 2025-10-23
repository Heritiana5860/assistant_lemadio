import 'package:flutter/material.dart';
import '../config/constants.dart';
import 'chat_screen.dart';

/// Écran d'accueil avec introduction et questions suggérées
class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(AppSizes.paddingLarge),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // En-tête avec logo
              _buildHeader(),

              const SizedBox(height: AppSizes.paddingLarge * 2),

              // Message de bienvenue
              _buildWelcomeCard(),

              const SizedBox(height: AppSizes.paddingLarge),

              // Bouton principal
              _buildStartButton(context),

              const SizedBox(height: AppSizes.paddingLarge * 2),

              // Section questions suggérées
              _buildSuggestedQuestionsSection(context),

              const SizedBox(height: AppSizes.paddingLarge),

              // Section informations
              _buildInfoSection(),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildHeader() {
    return Column(
      children: [
        // Logo/Icône
        Container(
          width: 100,
          height: 100,
          decoration: BoxDecoration(
            color: AppColors.primary,
            borderRadius: BorderRadius.circular(24),
            boxShadow: [
              BoxShadow(
                color: AppColors.primary.withOpacity(0.3),
                blurRadius: 20,
                offset: const Offset(0, 10),
              ),
            ],
          ),
          child: const Icon(Icons.smart_toy, size: 56, color: Colors.white),
        ),

        const SizedBox(height: AppSizes.paddingMedium),

        // Titre
        const Text(
          AppStrings.appName,
          style: AppTextStyles.heading1,
          textAlign: TextAlign.center,
        ),

        const SizedBox(height: AppSizes.paddingSmall),

        // Sous-titre
        Text(
          AppStrings.appSubtitle,
          style: AppTextStyles.bodySmall,
          textAlign: TextAlign.center,
        ),
      ],
    );
  }

  Widget _buildWelcomeCard() {
    return Container(
      padding: const EdgeInsets.all(AppSizes.paddingLarge),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [AppColors.primary, AppColors.primaryDark],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(AppSizes.borderRadius),
        boxShadow: [
          BoxShadow(
            color: AppColors.primary.withOpacity(0.3),
            blurRadius: 15,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: const [
              Icon(Icons.waving_hand, color: Colors.amber, size: 32),
              SizedBox(width: AppSizes.paddingSmall),
              Expanded(
                child: Text(
                  AppStrings.welcomeTitle,
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: AppSizes.paddingMedium),

          const Text(
            AppStrings.welcomeMessage,
            style: TextStyle(fontSize: 16, color: Colors.white, height: 1.5),
          ),
        ],
      ),
    );
  }

  Widget _buildStartButton(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => const ChatScreen()),
        );
      },
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.primary,
        foregroundColor: Colors.white,
        padding: const EdgeInsets.symmetric(
          vertical: AppSizes.paddingMedium + 4,
        ),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(AppSizes.borderRadius),
        ),
        elevation: 4,
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: const [
          Icon(Icons.chat_bubble_outline, size: AppSizes.iconSize),
          SizedBox(width: AppSizes.paddingSmall),
          Text(
            AppStrings.startButton,
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),
        ],
      ),
    );
  }

  Widget _buildSuggestedQuestionsSection(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text('Questions fréquentes', style: AppTextStyles.heading2),

        const SizedBox(height: AppSizes.paddingSmall),

        const Text(
          'Cliquez sur une question pour commencer',
          style: AppTextStyles.bodySmall,
        ),

        const SizedBox(height: AppSizes.paddingMedium),

        ...AppStrings.suggestedQuestions.map(
          (question) => _buildSuggestedQuestionCard(context, question),
        ),
      ],
    );
  }

  Widget _buildSuggestedQuestionCard(BuildContext context, String question) {
    return Container(
      margin: const EdgeInsets.only(bottom: AppSizes.paddingSmall),
      child: Material(
        color: AppColors.cardBackground,
        borderRadius: BorderRadius.circular(AppSizes.borderRadius),
        child: InkWell(
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (_) => ChatScreen(initialMessage: question),
              ),
            );
          },
          borderRadius: BorderRadius.circular(AppSizes.borderRadius),
          child: Padding(
            padding: const EdgeInsets.all(AppSizes.paddingMedium),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: AppColors.primary.withOpacity(0.1),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: const Icon(
                    Icons.help_outline,
                    color: AppColors.primary,
                    size: AppSizes.iconSize,
                  ),
                ),

                const SizedBox(width: AppSizes.paddingMedium),

                Expanded(child: Text(question, style: AppTextStyles.body)),

                const Icon(
                  Icons.arrow_forward_ios,
                  size: 16,
                  color: AppColors.textSecondary,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildInfoSection() {
    return Container(
      padding: const EdgeInsets.all(AppSizes.paddingLarge),
      decoration: BoxDecoration(
        color: AppColors.info.withOpacity(0.1),
        borderRadius: BorderRadius.circular(AppSizes.borderRadius),
        border: Border.all(color: AppColors.info.withOpacity(0.3), width: 1),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: const [
              Icon(
                Icons.info_outline,
                color: AppColors.info,
                size: AppSizes.iconSize,
              ),
              SizedBox(width: AppSizes.paddingSmall),
              Text(
                'À savoir',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: AppColors.info,
                ),
              ),
            ],
          ),

          const SizedBox(height: AppSizes.paddingMedium),

          _buildInfoItem(
            Icons.verified_outlined,
            'Réponses basées sur la documentation officielle ADES',
          ),

          const SizedBox(height: AppSizes.paddingSmall),

          _buildInfoItem(
            Icons.access_time,
            'Disponible 24/7, même hors ligne après la première utilisation',
          ),

          const SizedBox(height: AppSizes.paddingSmall),

          _buildInfoItem(
            Icons.update,
            'Mis à jour régulièrement avec les nouvelles fonctionnalités',
          ),
        ],
      ),
    );
  }

  Widget _buildInfoItem(IconData icon, String text) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Icon(icon, size: 20, color: AppColors.info),
        const SizedBox(width: AppSizes.paddingSmall),
        Expanded(
          child: Text(
            text,
            style: const TextStyle(
              fontSize: 14,
              color: AppColors.textPrimary,
              height: 1.4,
            ),
          ),
        ),
      ],
    );
  }
}
