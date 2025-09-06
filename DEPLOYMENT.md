# Deployment Guide - Voice Agent with Coolify

This guide explains how to deploy the IRS Conspiracy Voice Agent using Coolify for automated CI/CD.

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Next.js App   │    │  LiveKit Server  │    │  Python Agent   │
│   (Frontend)    │◄──►│   Port: 7880     │◄──►│   (Backend)     │
│   Port: 3000    │    └──────────────────┘    └─────────────────┘
└─────────────────┘                                                
```

## Prerequisites

1. **Coolify** installed and running on your server
2. **GitHub repository** with this codebase
3. **API Keys** for AI services (Deepgram, Groq, ElevenLabs)

## Local Testing with Docker

Before deploying to Coolify, test locally:

1. **Copy environment file:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

2. **Build and run:**
   ```bash
   docker-compose up --build
   ```

3. **Access:**
   - Frontend: http://localhost:3000
   - LiveKit: http://localhost:7880

## Coolify Deployment

### 1. Access Coolify Dashboard

- URL: `http://your-server-ip:8000`
- Create new project: "Voice Agent"

### 2. Configure GitHub Integration

1. **Connect Repository:**
   - Repository: `https://github.com/Mahir-Isikli/voice-therapy-app.git`
   - Branch: `main`
   - Enable auto-deployment on push

### 3. Create Services

#### A. LiveKit Server Service

**Type:** Docker Compose Service
```yaml
version: '3.8'
services:
  livekit:
    image: livekit/livekit-server:latest
    command: --dev
    ports:
      - "7880:7880"
      - "7881:7881"
    environment:
      - LIVEKIT_KEYS=devkey:secret
```

#### B. Backend Service (Python Agent)

**Type:** Docker Service
- **Build Context:** `./backend`
- **Dockerfile:** `./backend/Dockerfile`
- **Environment Variables:**
  ```
  LIVEKIT_URL=ws://livekit:7880
  LIVEKIT_API_KEY=devkey
  LIVEKIT_API_SECRET=secret
  DEEPGRAM_API_KEY=your_key
  GROQ_API_KEY=your_key
  ELEVEN_API_KEY=your_key
  ```

#### C. Frontend Service (Next.js)

**Type:** Docker Service
- **Build Context:** `./frontend`
- **Dockerfile:** `./frontend/Dockerfile`
- **Port Mapping:** `3000:3000`
- **Environment Variables:**
  ```
  LIVEKIT_URL=wss://your-domain.com:7880
  LIVEKIT_API_KEY=devkey
  LIVEKIT_API_SECRET=secret
  ```
- **Domain:** `your-domain.com`

### 4. Service Configuration

#### Resource Limits
- **Frontend:** 512MB RAM, 0.5 CPU
- **Backend:** 1GB RAM, 1 CPU  
- **LiveKit:** 1GB RAM, 1 CPU

#### Health Checks
All services include health checks in their Dockerfiles.

#### Networking
Services communicate via Coolify's internal network.

### 5. Domain & SSL

1. **Configure Domain:**
   - Point `your-domain.com` to server IP
   - Configure in Coolify dashboard

2. **SSL Certificates:**
   - Coolify auto-generates Let's Encrypt certificates
   - Ensure ports 80/443 are accessible

## Migration from PM2

### 1. Test New Deployment
Deploy to staging subdomain first to verify functionality.

### 2. Switch Traffic
1. Stop current PM2 processes:
   ```bash
   pm2 stop jopyter-frontend jopyter-agent livekit-server
   ```
2. Update DNS/proxy to point to Coolify services
3. Test thoroughly

### 3. Cleanup Old Deployment
Once confirmed working:
```bash
pm2 delete jopyter-frontend jopyter-agent livekit-server
# Archive old directories
mv /opt/jopyter /opt/jopyter-backup-$(date +%Y%m%d)
mv /opt/jopyter-voice-agent /opt/jopyter-voice-agent-backup-$(date +%Y%m%d)
```

## Environment Variables Reference

### Production Frontend (.env)
```bash
LIVEKIT_URL=wss://your-domain.com:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
```

### Production Backend (.env)
```bash
LIVEKIT_URL=ws://livekit:7880  # Internal service name
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
DEEPGRAM_API_KEY=your_actual_key
GROQ_API_KEY=your_actual_key
ELEVEN_API_KEY=your_actual_key
```

## Troubleshooting

### Build Issues
- Check Dockerfile syntax
- Verify all required files are present
- Check .dockerignore isn't excluding needed files

### Connection Issues
- Verify LiveKit server is running
- Check network connectivity between services
- Verify firewall rules for ports 7880-7881

### Audio Issues
- Ensure WebRTC ports (7882-8000) are open
- Check STUN/TURN configuration
- Verify SSL certificates are working

## Monitoring

Coolify provides:
- **Resource Usage:** CPU, RAM, disk
- **Service Logs:** Real-time log viewing
- **Health Status:** Service uptime monitoring
- **Deployment History:** Easy rollbacks

## Backup Strategy

1. **Database:** None required (stateless services)
2. **Code:** Stored in GitHub
3. **Environment Variables:** Backed up in Coolify
4. **Logs:** Retained for 7 days in Coolify

## Next Steps

After successful deployment:

1. **Setup Staging:** Create staging environment for testing
2. **Monitoring:** Configure alerting for service failures  
3. **Scaling:** Add load balancing if traffic increases
4. **Security:** Review and harden security settings