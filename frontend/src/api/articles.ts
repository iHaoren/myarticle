import axios from "axios";
import type { Article } from "../types/article";

const BASE_URL = 'http://127.0.0.1:5000'

// fungsi untuk ambil artikel
export const getArticles = async (): Promise<Article[]> => {
  const response = await axios.get(`${BASE_URL}/articles`)
  return response.data
};

// ambil satu artikel berdasarkan id
export const getArticle = async (id:number): Promise<Article> => {
  const response = await axios.get(`${BASE_URL}/articles/${id}`)
  return response.data
}