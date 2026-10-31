flowchart TD
    subgraph Mobile ["📱 Client Layer"]
        A[Mobile App / Text Sender]
    end

    subgraph Backend ["⚡ FastAPI & Classification Layer"]
        B[FastAPI Endpoint]
        C[spaCy Text Classification]
    end

    subgraph Queue ["🔄 Task Processing Layer"]
        D[Celery Async Task Queue]
    end

    subgraph Tools ["🛠️ Intent Handlers / Tools"]
        E1[Time Handler]
        E2[Weather Handler]
        E3[Currency Handler]
        E4[Gemini Q&A Handler]
    end

    subgraph Speech ["🎙️ TTS & Storage Layer"]
        F[Amazon Polly Service + Caching]
        G[(Local File System / Storage)]
    end

    subgraph Hardware ["🤖 IoT Output Layer"]
        H[MQTT Broker / Mosquitto]
        I[ESP32 Audio Player]
    end

    %% Data Flow
    A -->|1. Send Text Input| B
    B -->|2. Extract Intent| C
    C -->|3. Dispatch Job| D
    
    D -->|Intent: Time| E1
    D -->|Intent: Weather| E2
    D -->|Intent: Currency| E3
    D -->|Intent: Others| E4

    E1 -->|Text Result| F
    E2 -->|Text Result| F
    E3 -->|Text Result| F
    E4 -->|Text Result| F

    F -->|Save MP3| G
    F -->|Publish Audio Ready Event| H
    H -->|MQTT Topic Notification| I
    I -->|HTTP Stream Audio Request| B
    B -->|Stream MP3 Payload| G
