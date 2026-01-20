from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage
import os
from models import LLMProviderEnum

class LLMService:
    def __init__(self):
        self.providers = {}
        
    def get_llm(self, provider: LLMProviderEnum):
        if provider == LLMProviderEnum.AUTO:
            provider = LLMProviderEnum.GPT35
        
        if provider in [LLMProviderEnum.GPT4, LLMProviderEnum.GPT35]:
            model = "gpt-4" if provider == LLMProviderEnum.GPT4 else "gpt-3.5-turbo"
            return ChatOpenAI(model=model, temperature=0.7)
        
        elif provider == LLMProviderEnum.CLAUDE:
            return ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.7)
        
        elif provider in [LLMProviderEnum.LLAMA, LLMProviderEnum.MISTRAL, LLMProviderEnum.PHI]:
            from langchain_community.llms import Ollama
            model_map = {
                LLMProviderEnum.LLAMA: "llama2",
                LLMProviderEnum.MISTRAL: "mistral",
                LLMProviderEnum.PHI: "phi"
            }
            return Ollama(model=model_map[provider])
        
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    
    def generate_lesson(self, learner_profile: dict, subject: str, grade: int, provider: LLMProviderEnum):
        llm = self.get_llm(provider)
        
        system_prompt = f"""You are Oola, an expert AI teacher specializing in personalized education.
        
Student Profile:
- Grade: {grade}
- Subject: {subject}
- Learning Style: {learner_profile.get('learning_style', 'visual')}
- Strengths: {learner_profile.get('strengths', [])}
- Areas for Growth: {learner_profile.get('weaknesses', [])}
- Special Needs: {learner_profile.get('special_needs', {})}

Create an engaging, age-appropriate lesson using real-world examples and analogies that match this student's learning style.
Keep it interactive and encourage critical thinking."""

        user_prompt = f"Create a {subject} lesson for grade {grade}. Make it practical and engaging."
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = llm.invoke(messages)
        return response.content if hasattr(response, 'content') else str(response)
    
    def chat_with_student(self, message: str, context: dict, provider: LLMProviderEnum):
        llm = self.get_llm(provider)
        
        system_prompt = f"""You are Oola, a friendly and encouraging AI teacher.
        
Current Context:
- Student: {context.get('learner_name')}
- Grade: {context.get('grade')}
- Subject: {context.get('subject', 'General')}
- Learning Style: {context.get('learning_style', 'visual')}

Be supportive, ask questions to check understanding, and adapt explanations to the student's level.
Use analogies and real-world examples. Encourage the student to explain concepts back to you."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=message)
        ]
        
        response = llm.invoke(messages)
        return response.content if hasattr(response, 'content') else str(response)

llm_service = LLMService()
