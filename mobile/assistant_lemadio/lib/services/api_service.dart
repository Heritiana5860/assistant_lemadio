import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/message.dart';

/// Service pour communiquer avec le backend ADES
class ApiService {
  // ⚠️ IMPORTANT : Changez cette URL selon votre configuration
  // - Si vous testez sur émulateur Android : http://10.0.2.2:3000
  // - Si vous testez sur appareil réel : http://VOTRE_IP_LOCAL:3000
  // - En production : https://votre-serveur.com
  static const String baseUrl = 'http://192.168.1.52:3000';

  /// Envoie un message au chatbot et retourne la réponse
  Future<Message> sendMessage(String userMessage) async {
    try {
      final url = Uri.parse('$baseUrl/api/chat');

      final response = await http
          .post(
            url,
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode({'message': userMessage}),
          )
          .timeout(
            const Duration(seconds: 60), // Timeout de 60 secondes
          );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);

        return Message.bot(
          data['reply'] as String,
          ragUsed: data['rag_used'] as bool? ?? false,
        );
      } else {
        throw Exception('Erreur serveur: ${response.statusCode}');
      }
    } on http.ClientException {
      throw Exception(
        'Erreur de connexion: Impossible de joindre le serveur. Vérifiez votre connexion internet.',
      );
    } on TimeoutException {
      throw Exception(
        'Le serveur met trop de temps à répondre. Veuillez réessayer.',
      );
    } catch (e) {
      throw Exception('Erreur inattendue: $e');
    }
  }

  /// Vérifie la santé du backend
  Future<Map<String, dynamic>> checkHealth() async {
    try {
      final url = Uri.parse('$baseUrl/api/health');

      final response = await http.get(url).timeout(const Duration(seconds: 10));

      if (response.statusCode == 200) {
        return jsonDecode(response.body) as Map<String, dynamic>;
      } else {
        return {'backend': 'error', 'ollama': 'error', 'rag': 'error'};
      }
    } catch (e) {
      return {
        'backend': 'disconnected',
        'ollama': 'disconnected',
        'rag': 'disconnected',
        'error': e.toString(),
      };
    }
  }

  /// Teste la recherche RAG (pour déboguer)
  Future<List<String>> searchDocumentation(String query) async {
    try {
      final url = Uri.parse('$baseUrl/api/search');

      final response = await http
          .post(
            url,
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode({'query': query, 'top_k': 3}),
          )
          .timeout(const Duration(seconds: 10));

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final results = data['results'] as List;

        return results.map((r) => r['preview'] as String).toList();
      } else {
        return [];
      }
    } catch (e) {
      print('Erreur recherche: $e');
      return [];
    }
  }
}
