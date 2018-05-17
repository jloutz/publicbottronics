## meet n' greet
* greet
    - utter_greet
    > handle_user_query

## general help
> handle_user_query
* need_help_general
    - utter_general_help
    > handle_user_query

## how to publish?
> handle_user_query
* ask_about_publish
    - utter_inform_publish
    > ask_start_questionaire

## ask start questionaire
> ask_start_questionaire
- ask_start_questionaire_eingabeverfahren
> handle_answer_start_questionaire

## handle answer start questionaire
> handle_answer_start_questionaire
* affirm
    - utter_start_questionaire_eingabeverfahren
    - utter_ask_num_courses
    > handle_user_info

## handle answer start questionaire
> handle_answer_start_questionaire
* deny
    - utter_acknowledge_deny
    - utter_noch_fragen
    > handle_noch_fragen

    
## num courses
> handle_user_info
* inform{"anz_kuerse":"29"}
    - utter_ask_change_freq
    > handle_user_info

## change freq
> handle_user_info
* inform{"change_freq":"wöchentlich"}
    - ActionEvalEingabekanal
    > eingabekanal_empfehlung

## change freq
> handle_user_info
* inform{"change_freq":"täglich"}
    - ActionEvalEingabekanal
    > eingabekanal_empfehlung

## change freq
> handle_user_info
* inform{"change_freq":"monatlich"}
    - ActionEvalEingabekanal
    > eingabekanal_empfehlung

## change freq
> handle_user_info
* inform{"change_freq":"selten"}
    - ActionEvalEingabekanal
    > eingabekanal_empfehlung


## recommend kanal
> eingabekanal_empfehlung{"empfohlenes_kanal":"online"}
  - utter_recommend_online
  - utter_recommend_online_clarify
  - utter_ask_aufwand_ok
  > handle_user_info

## recommend kanal
> eingabekanal_empfehlung{"empfohlenes_kanal":"xml"}
  - utter_recommend_xml
  - utter_recommend_xml_clarify
  - utter_ask_aufwand_ok
  > handle_user_info

## aufwand ok
> handle_user_info
* inform("aufwand_ok":"ja")
  - ActionEvalEingabeverfahren
  > recommend_verfahren

## aufwand nok
> handle_user_info
* inform("aufwand_ok":"nein")
  - ActionEvalEingabeverfahren
  > recommend_verfahren

## recommend verfahren
> recommend_verfahren{"empfohlenes_verfahren":"xml"}
  - utter_recommend_xml
  - utter_noch_fragen
  > handle_noch_fragen

## recommend verfahren
> recommend_verfahren{"empfohlenes_verfahren":"online"}
  - utter_recommend_online
  - utter_noch_fragen
  > handle_noch_fragen

## recommend verfahren
> recommend_verfahren{"empfohlenes_verfahren":"extern"}
  - utter_recommend_extern
  - utter_noch_fragen
  > handle_noch_fragen

## recommend verfahren
> recommend_verfahren{"empfohlenes_verfahren":"redaktion"}
  - utter_recommend_redaktion
  - utter_noch_fragen
  > handle_noch_fragen


## handle noch fragen
> handle_noch_fragen
* affirm
  - utter_how_help
  > handle_user_query

## handle noch fragen
> handle_noch_fragen
* deny
  - utter_acknowledge_affirm
  - utter_goodbye

## allgemeine hilfe
> handle_user_query
* ask_help
  - utter_inform_help
  > handle_user_query

## need help no questionaire
* greet
    - utter_greet
* need_help_general
    - utter_general_help 
* ask_about_publish
   - utter_inform_publish
   - ask_start_questionaire_eingabeverfahren
* deny
    - utter_acknowledge_deny
    - utter_noch_fragen
    > handle_noch_fragen

## need help start questionaire
* greet
    - utter_greet
* need_help_general
    - utter_general_help 
* ask_about_publish
   - utter_inform_publish
   - ask_start_questionaire_eingabeverfahren
* affirm
    - utter_start_questionaire_eingabeverfahren
    - utter_ask_num_courses
* inform{"anz_kuerse": "30"}
    - slot{"anz_kuerse": "30"}
    - utter_ask_change_freq
* inform{"change_freq": "wöchentlich"}
    - slot{"change_freq": "wöchentlich"}
    - ActionEvalEingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_recommend_online_clarify
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - ActionEvalEingabeverfahren
    - slot{"empfohlenes_verfahren": "online"}
    - utter_recommend_online
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## low volume aufwand ok
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - ask_start_questionaire_eingabeverfahren
* affirm
    - utter_start_questionaire_eingabeverfahren
    - utter_ask_num_courses
* inform{"anz_kuerse": "30"}
    - slot{"anz_kuerse": "30"}
    - utter_ask_change_freq
* inform{"change_freq": "wöchentlich"}
    - slot{"change_freq": "wöchentlich"}
    - ActionEvalEingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_recommend_online_clarify
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - ActionEvalEingabeverfahren
    - slot{"empfohlenes_verfahren": "online"}
    - utter_recommend_online
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## low volume aufwand nok 
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - ask_start_questionaire_eingabeverfahren
* affirm
    - utter_start_questionaire_eingabeverfahren
    - utter_ask_num_courses
* inform{"anz_kuerse": "30"}
    - slot{"anz_kuerse": "30"}
    - utter_ask_change_freq
* inform{"change_freq": "wöchentlich"}
    - slot{"change_freq": "wöchentlich"}
    - ActionEvalEingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_recommend_online_clarify
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - ActionEvalEingabeverfahren
    - slot{"empfohlenes_verfahren": "redaktion"}
    - utter_recommend_redaktion
    - utter_noch_fragen
* affirm
    - utter_how_help
    > handle_user_query


## high volume aufwand nok 2
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - ask_start_questionaire_eingabeverfahren
* affirm
    - utter_start_questionaire_eingabeverfahren
    - utter_ask_num_courses
* inform{"anz_kuerse": "60"}
    - slot{"anz_kuerse": "60"}
    - utter_ask_change_freq
* inform{"change_freq": "täglich"}
    - slot{"change_freq": "täglich"}
    - ActionEvalEingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_recommend_xml_clarify
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - ActionEvalEingabeverfahren
    - slot{"empfohlenes_verfahren": "extern"}
    - utter_recommend_extern
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## high volume aufwand nok 2
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - ask_start_questionaire_eingabeverfahren
* affirm
    - utter_start_questionaire_eingabeverfahren
    - utter_ask_num_courses
* inform{"anz_kuerse": "60"}
    - slot{"anz_kuerse": "60"}
    - utter_ask_change_freq
* inform{"change_freq": "wöchentlich"}
    - slot{"change_freq": "wöchentlich"}
    - ActionEvalEingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_recommend_xml_clarify
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - ActionEvalEingabeverfahren
    - slot{"empfohlenes_verfahren": "extern"}
    - utter_recommend_extern
    - utter_noch_fragen
    > handle_noch_fragen

## high volume aufwand ok
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - ask_start_questionaire_eingabeverfahren
* affirm
    - utter_start_questionaire_eingabeverfahren
    - utter_ask_num_courses
* inform{"anz_kuerse": "100"}
    - slot{"anz_kuerse": "100"}
    - utter_ask_change_freq
* inform{"change_freq": "täglich"}
    - slot{"change_freq": "täglich"}
    - ActionEvalEingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_recommend_xml_clarify
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - ActionEvalEingabeverfahren
    - slot{"empfohlenes_verfahren": "xml"}
    - utter_recommend_xml
    - utter_noch_fragen
* affirm
    - utter_how_help
    > handle_user_query

